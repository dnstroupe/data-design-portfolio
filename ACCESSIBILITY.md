# Accessibility notes

I want the site to work for people who navigate and read in different ways. These notes separate what is in place from what still needs a closer look.

## In place

* HTML language and viewport settings on every page.
* One main heading per page, with headings for the sections below it.
* Header, navigation, main content, and footer landmarks.
* A skip link and visible focus styles for keyboard navigation.
* Text labels alongside the interface illustrations, so color is not the only way information is communicated.
* A single column layout on smaller screens. Supporting panels remain available on phones.
* Reduced motion support for smooth scrolling.
* System fonts, with no external font download.

## Checks

The local check script verifies page structure, internal links, fragments, and selected color pairs. The browser checks are recorded in CHECKS.md.

A passing script is only a starting point. It cannot tell us whether the reading order makes sense to a screen reader user or whether the case studies are clear.

## Still to do

* Read every page with VoiceOver and record any confusing announcements or navigation.
* Check every link and the skip link using only a keyboard.
* Check text zoom at 200 percent and reflow at 400 percent.
* Test on actual phones and in more than one browser.
* Review the illustrations with someone who uses assistive technology.
* Complete a formal review before making any Section 508 conformance claim.

The accessibility work described in the operational dashboard case study is separate from testing this website. That work covered keyboard navigation, focus order, contrast, hover feedback, and tooltips. It did not include a formal accessibility review or confirmed screen reader testing.

If something on the site gets in your way, [contact me on LinkedIn](https://www.linkedin.com/in/david-stroupe/) with the page and what happened.
