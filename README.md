# Portfolio

Jekyll site. GitHub Pages builds it automatically; no local setup needed.

## Edit
- **Blog post:** add `_posts/YYYY-MM-DD-slug.md` with front matter `layout: post`, `title:`, optional `description:`.
- **Project:** add a block to `_data/work.yml` (`featured: true` shows it on Home).
- **About rows:** `_data/about.yml`.
- **Nav, email, social links, domain:** `_config.yml`.
- **New page:** copy `about.html`, change `title` and `permalink`, add to `nav` in `_config.yml`.
- **Extra data:** add any YAML file to `_data/` and read it as `site.data.<filename>`.

## Publish with a custom domain
1. Put your domain in `CNAME` (one line) and in `url:` in `_config.yml`.
2. Push to a repo. Settings > Pages > Deploy from branch > `main` / root.
3. DNS: apex domain gets four A records (185.199.108.153, .109.153, .110.153, .111.153); `www` gets a CNAME to `<user>.github.io`.
4. Settings > Pages > enable Enforce HTTPS once the certificate is issued.
