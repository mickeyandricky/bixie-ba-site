#!/bin/bash
# Deploy bixie.ba to Cloudflare Pages
# Usage: ./deploy.sh

set -e

SITE_DIR="/root/bixie-site"
echo "🚀 Deploying bixie.ba to Cloudflare Pages..."

# Check if wrangler is installed
if ! command -v wrangler &> /dev/null; then
    echo "Installing wrangler CLI..."
    npm install -g wrangler
fi

cd "$SITE_DIR"

# Optional: Check if logged in to Cloudflare
echo "📦 Building site..."
echo "   Site is static HTML, no build step needed."

echo "☁️ Deploying to Cloudflare Pages..."
wrangler pages deploy . --project-name=bixie-ba --branch=main

echo ""
echo "✅ Deployment complete!"
echo "   Site: https://bixie-ba.pages.dev"
echo "   Custom domain: https://bixie.ba (point Cloudflare DNS to Pages)"
