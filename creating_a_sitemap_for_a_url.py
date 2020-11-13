import pandas as pd
import os
import datetime
from jinja2 import Template
import gzip
list_of_urls = pd.read_csv('list_of_urls.csv')
list_of_urls
<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    {% for page in pages %}
    <url>
        <loc>{{page[1]|safe}}</loc>
        <lastmod>{{page[3]}}</lastmod>
        <changefreq>{{page[4]}}</changefreq>
        <priority>{{page[5]}}</priority>
    </url>
    {% endfor %}
</urlset>

template = Template(sitemap_template)
lastmod_date = datetime.datetime.now().strftime('%Y-%m-%d')

lastmod_date = datetime.datetime.now().strftime('%Y-%m-%d')
for i in new_df:                           # For each URL in the list of URLs ...
    i.loc[:,'lastmod'] = lastmod_date      # ... add Lastmod date
    i.loc[:,'changefreq'] = 'daily'        # ... add changefreq
    i.loc[:,'priority'] = '1.0'
    sitemap_output = template.render(pages = i.itertuples())
    filename = 'sitemap' + str(i.iloc[0,1]) + '.xml.gz'
    with gzip.open(filename, 'wt') as f:   
        f.write(sitemap_output)
