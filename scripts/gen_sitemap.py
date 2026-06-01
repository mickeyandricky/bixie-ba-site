#!/usr/bin/env python3
"""Update sitemap with all language variants."""
import re

SITE = 'https://bixie.ba'
sitemap_path = '/root/bixie-site/sitemap.xml'

with open(sitemap_path) as f:
    sitemap = f.read()

# Remove old content and rebuild
sitemap = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
'''

pages = [
    ('', 1.0, 'weekly'),
    ('about', 0.8, 'monthly'),
    ('services/crm', 0.9, 'monthly'),
    ('services/ai-agents', 0.9, 'monthly'),
    ('services/digital-transformation', 0.9, 'monthly'),
    ('services/rpa', 0.8, 'monthly'),
    ('ai-providers', 0.8, 'monthly'),
    ('blog', 0.8, 'weekly'),
    ('contact', 0.7, 'monthly'),
    ('privacy', 0.3, 'yearly'),
]

blog_posts = [
    'ai-licence-obrazovne-ustanove',
    'bitrix24-vs-ai-crm',
    'rpa-automatizacija-procesa',
    'bitrix24-crm-implementacija-vodic',
    'salesforce-crm-implementacija',
    'zoho-crm-implementacija',
    'monday-crm-produktivnost',
    'ai-agenti-customer-support',
    'agentic-ai-autonomni-agenti',
]

for lang, prefix in [('bs', ''), ('en', 'en/'), ('de', 'de/')]:
    for rel, priority, freq in pages:
        url = f'{SITE}/{prefix}{rel}' if rel else f'{SITE}/{prefix}'.rstrip('/')
        sitemap += f'  <url>\n    <loc>{url}</loc>\n    <priority>{priority}</priority>\n    <changefreq>{freq}</changefreq>\n'
        
        # Add hreflang alternates for all 3 languages
        for l, p in [('en', 'en/'), ('de', 'de/'), ('bs', ''), ('x-default', '')]:
            alt_url = f'{SITE}/{p}{rel}' if rel else f'{SITE}/{p}'.rstrip('/')
            sitemap += f'    <xhtml:link rel="alternate" hreflang="{l}" href="{alt_url}"/>\n'
        
        sitemap += '  </url>\n'

# Blog posts (BS only)
for post in blog_posts:
    url = f'{SITE}/blog/posts/{post}'
    sitemap += f'  <url>\n    <loc>{url}</loc>\n    <priority>0.6</priority>\n    <changefreq>monthly</changefreq>\n'
    for l, p in [('en', 'en/'), ('de', 'de/'), ('bs', ''), ('x-default', '')]:
        alt_url = f'{SITE}/{p}blog/posts/{post}'
        sitemap += f'    <xhtml:link rel="alternate" hreflang="{l}" href="{alt_url}"/>\n'
    sitemap += '  </url>\n'

sitemap += '</urlset>'

with open(sitemap_path, 'w') as f:
    f.write(sitemap)

# Count URLs
url_count = sitemap.count('<loc>')
print(f'Sitemap updated: {url_count} URLs')
