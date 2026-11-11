# Data & Interface

I build dashboards and reporting tools for government teams and senior leaders. This is my portfolio, part of a fresh start for my GitHub.

The site brings together my background in data visualization, workflow automation, and operational applications. I am also developing my UX practice through the Google UX Design course and learning Figma.

[Visit the portfolio](https://dnstroupe.github.io/data-design-portfolio/) · [Connect on LinkedIn](https://www.linkedin.com/in/david-stroupe/)

## What I wanted this site to do

Someone should be able to open it, understand the work I do, and see how I approach a problem. A list of tools would only tell part of that story. The case studies explain the request, what I contributed, the choices I made, and where the work stands.

## What is inside

* Operational dashboards: taking a request to recreate SharePoint sites and building a more useful experience in Foundry Workshop.
* Executive reporting: bringing a recurring leadership reporting process into Power BI.
* Request intake: using Power Automate and SharePoint to handle incoming information.
* Performance tracking: connecting day to day records with reporting and review needs.

These are summaries of professional experience. The code in this repository is for the portfolio website, not the applications described in those summaries. All interface illustrations use fictional content. There are no customer screenshots, operational datasets, or government application files here.

## My role and how this site was made

I provided the work history, explained my role and decisions, and chose the visual direction. I used an AI assistant to help organize the writing and build the website. The site is not being presented as a Figma deliverable or as code I wrote entirely by hand.

The visual direction uses charcoal, a small amount of teal, straightforward typography, and plenty of space. The work should be the focus. There are no stock photos, animated skill bars, or invented testimonials.

## Run it locally

The website is plain HTML and CSS. There are no packages to install and no build service to configure.

From this folder, run:

```sh
python3 -m http.server 8000
```

Then open `http://localhost:8000` in your browser. Stop the server with Control + C when you are done.

The checked in HTML and CSS are ready to publish. To change the content or shared layout, edit `build_portfolio.py`, then run:

```sh
python3 build_portfolio.py
python3 check_site.py
```

The build script rewrites the seven HTML pages and `style.css`. Make lasting changes in the script rather than editing the generated pages alone.

## A few useful places to start

| File | What it covers |
| --- | --- |
| `index.html` | Introduction and selected work |
| `operations.html` | Current dashboard work |
| `reporting.html`, `automation.html`, `portal.html` | Earlier reporting and workflow experience |
| `about.html` | Background and approach |
| `accessibility.html` | Public accessibility statement |
| [DESIGN.md](DESIGN.md) | Why the site looks and reads this way |
| [ACCESSIBILITY.md](ACCESSIBILITY.md) | Checks, limits, and remaining work |
| [ROADMAP.md](ROADMAP.md) | Small improvements to tackle next |
| [CHECKS.md](CHECKS.md) | What was checked before publishing |

## Publishing

GitHub Pages serves the files from the root of the `main` branch. Relative links keep the pages working under the repository URL. There is no database, login, contact form, analytics, or API key to maintain. Contact links go to LinkedIn.

## Where it goes next

The next step is to add real design artifacts as I complete them: a Figma flow, wireframes, a prototype, and notes from testing. I want the repository to show how the work develops, not just the finished screen.

This portfolio has not had a formal Section 508 conformance review. The accessibility notes explain the checks and what remains.

## Featured independent project

[Operations Overview](https://github.com/dnstroupe/operations-overview) is my first featured dashboard project. It includes editable Figma layouts, a working demo with fictional data, and a case study. The portfolio links to it separately from my professional experience summaries.
