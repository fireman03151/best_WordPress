<p align="center"><img src="https://raw.githubusercontent.com/WordOps/WordOps/master/logo.png" width="400" alt="Wordops" /><a href="https://wordops.net">

  <br>
</p>

<h2 align="center">An essential toolset that eases WordPress site and server administration</h2>

<p align="center">
<img src="https://img.virtubox.net/images/2019/03/27/wordops-stable-4.mp4.gif" width="600" alt="WordOps" />

</p>

<p align="center">
<a href="https://travis-ci.org/WordOps/WordOps" target="_blank"><img src="https://travis-ci.org/WordOps/WordOps.svg?branch=master" alt="build"></a>
<img src="https://img.shields.io/github/license/wordops/wordops.svg" alt="MIT">
<img src="https://img.shields.io/github/last-commit/wordops/wordops.svg" alt="Commits">
<img alt="GitHub release" src="https://img.shields.io/github/release/WordOps/WordOps.svg">
<br><img src="https://netdata.wordops.eu/netdata/api/v1/badge.svg?chart=web_log_wops.cc.requests_per_url&options=unaligned&dimensions=download&group=sum&after=-86400&label=today&units=installations&precision=0&value_color=%230055AA" alt >
<a href="https://www.codacy.com/app/VirtuBox/WordOps?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=WordOps/WordOps&amp;utm_campaign=Badge_Grade"><img src="https://api.codacy.com/project/badge/Grade/fe9100fd2c634de7882ecec17f00a11a"/></a>
<a href="https://twitter.com/WordOps_" target="_blank"><img src="https://img.shields.io/badge/twitter-%40WordOps__-blue.svg?style=flat&logo=twitter" alt="Badge Twitter" /></a>
<a href="https://community.wordops.net/slack" target="_blank"><img src="https://img.shields.io/badge/slack-WordOps-4A154B.svg?style=flat&logo=slack" alt="Badge Slack" /></a>

</p>

<p align="center">
  <a href="#key-features">Key Features</a> •
  <a href="#usage">Usage</a> •
  <a href="https://github.com/WordOps/WordOps/projects">RoadMap</a> •
  <a href="https://github.com/WordOps/WordOps/blob/master/CHANGELOG.md">Changelog</a> •
  <a href="#credits">Credits</a> •
  <a href="#license">License</a>
</p>
<p align="center">
<a href="https://wordops.net" target="_blank"> WordOps.net</a> •
<a href="https://docs.wordops.net" target="_blank">Documentation</a> •
<a href="https://community.wordops.net" target="_blank">Community forum</a> •
<a href="https://demo.wordops.eu" target="_blank">Dashboard demo</a>
</p>

---

## Key Features

- **Easy to install** : One step automated installer with migration from EasyEngine v3 support
- **Fast deployment** : Fast and automated WordPress, Nginx, PHP, MySQL & Redis installation
- **Custom Nginx build** : Nginx 1.16.0 - TLS v1.3 Cloudflare HTTP/2 HPACK & Brotli support
- **Up-to-date** : PHP 7.2 & 7.3, MariaDB 10.3 & Redis 5.0
- **Secured** : Hardened WordPress security with strict Nginx location directives
- **Powerful** : Optimized Nginx configurations with multiple cache backends support
- **SSL** : Domain, Subdomain & Wildcard Let's Encrypt SSL certificates with DNS API handled by acme.sh
- **Modern** : Strong ciphers_suite, modern TLS protocols and HSTS support (Grade A+ on ssllabs)
- **Monitoring** : Live Nginx vhost traffic with ngx_vts_module and server monitoring with Netdata

## Requirements

### Operating System

- Ubuntu 16.04 LTS (Xenial)
- Ubuntu 18.04 LTS (Bionic)
- Ubuntu 19.04 (Disco)
- Debian 8 (Jessie)
- Debian 9 (Stretch)
- Debian 10 (Buster) - Not ready for production
- Raspbian 9 (Stretch)

### Ports requirements

- SSH (22 or custom)
- HTTP & HTTPS (80 & 443)
- WO Admin (22222)
- GPG key Server (11371 outbound)

## Getting Started

```bash
wget -qO wo wops.cc && sudo bash wo      # Install WordOps
sudo wo site create example.com --wp     # Install required packages & setup WordPress on example.com
```

## Must read

[From EasyEngine to WordOps](https://docs.wordops.net/about/from-easyengine-to-wordops/)

## Usage

### Standard WordPress sites

```bash
wo site create example.com --wp                  # install wordpress without any page caching
wo site create example.com --wp  --php73         # install wordpress with PHP 7.3  without any page caching
wo site create example.com --wpsc                # install wordpress with wp-super-cache plugin
wo site create example.com --wpfc                # install wordpress + nginx fastcgi_cache
wo site create example.com --wpredis             # install wordpress + nginx redis_cache
```

### WordPress multisite with subdirectory

```bash
wo site create example.com --wpsubdir            # install wpmu-subdirectory without any page caching
wo site create example.com --wpsubdir --wpsc     # install wpmu-subdirectory with wp-super-cache plugin
wo site create example.com --wpsubdir --wpfc     # install wpmu-subdirectory + nginx fastcgi_cache
wo site create example.com --wpsubdir --wpredis  # install wpmu-subdirectory + nginx redis_cache
```

### WordPress multisite with subdomain

```bash
wo site create example.com --wpsubdomain            # install wpmu-subdomain without any page caching
wo site create example.com --wpsubdomain --wpsc     # install wpmu-subdomain with wp-super-cache plugin
wo site create example.com --wpsubdomain --wpfc     # install wpmu-subdomain + nginx fastcgi_cache
wo site create example.com --wpsubdomain --wpredis  # install wpmu-subdomain + nginx redis_cache
```

### Non-WordPress sites

```bash
wo site create example.com --html     # create example.com for static/html sites
wo site create example.com --php      # create example.com with php support
wo site create example.com --mysql    # create example.com with php & mysql support
wo site create example.com --proxy=127.0.0.1:3000 #  create example.com with nginx as reverse-proxy
```

### Sites secured with Let's Encrypt

```bash
wo site create example.com --wp --letsencrypt #  wordpress secured with letsencrypt
wo site create sub.example.com --wp --letsencrypt=subdomain # wordpress + letsencrypt subdomain
wo site create site.tld --wp --letsencrypt --hsts # install wordpress & secure site with letsencrypt with HSTS
wo site create site.tld --wp --letsencrypt=wildcard --dns=dns_cf # install wordpress & issue a wildcard SSL certificate with Cloudflare DNS API
```

## Update WordOps

```bash
wo update
```

## Support

If you feel there is a bug directly related to WordOps, or if you want to suggest new features for WordOps, feel free to open an issue.
For any other questions about WordOps or if you need support, please use the [Community Forum](https://community.wordops.net/).

# Contributing

If you'd like to contribute, please fork the repository and make changes as you'd like. Pull requests are warmly welcome.
There is no need to be a developer or a system administrator to contribute to WordOps project. You can still contribute by helping us to improve [WordOps documentation](https://github.com/WordOps/docs.wordops.net).

## Credits

- Source : [EasyEngine](https://github.com/easyengine/easyengine)

Apps & Tools shipped with WordOps :

- [Acme.sh](https://github.com/Neilpang/acme.sh)
- [WP-CLI](https://github.com/wp-cli/wp-cli)
- [Netdata](https://github.com/netdata/netdata)
- [phpMyAdmin](https://www.phpmyadmin.net/)
- [Composer](https://github.com/composer/composer)
- [Adminer](https://www.adminer.org/)
- [phpRedisAdmin](https://github.com/erikdubbelboer/phpRedisAdmin)
- [opcacheGUI](https://github.com/amnuts/opcache-gui)
- [eXtplorer](https://github.com/soerennb/extplorer)
- [MySQLTuner](https://github.com/major/MySQLTuner-perl/)
- [Webgrind](https://github.com/jokkedk/webgrind)
- [MySQLTuner](https://github.com/major/MySQLTuner-perl)

## License

- [MIT](http://opensource.org/licenses/MIT) © [WordOps](https://wordops.net)
