# CS50 Project - Google Search

## Overview of the First Assignment: CSS, HTML, and SASS

A quick overview of the first assignment of CS50 Web Programming: a simple clone of Google Search, Google Image Search, and Google Advanced Search purely made with HTML and SCSS.

## Assignment Specification

- **Pages**: The website should have at least three pages: one for Google Search, one for Google Image Search, and one for Google Advanced Search.

  - On the Google Search page, there should be links in the upper-right of the page to go to Image Search or Advanced Search.
  - On the Image and Advanced search pages, there should also be links in the upper-right to go back to regular search or to visit each other.

- **Query Text**: Each page must have an input field for a query.

  - On the Google Search page, there should be an input field with id `q`.
  - On the Image and Advanced search pages, there should also be an input field with id `q`.

- **Query Button**: Each page must have a button that submits their respective form.

  - Like on real Google search results pages, this button could simply say "Google Search" or "I'm Feeling Lucky".

- **Query Submission**: When someone submits a form on any of these pages by hitting enter or clicking on a button:

  - The query text entered by the user should be sent as part of a GET request.

- **Lucky Button**: Add an "I'm Feeling Lucky" button to each search option that takes you directly into a random result based on your query.

- **Aesthetics**: The CSS you write should resemble CS50's aesthetics as closely as possible. For example:
  - Use similar fonts (like Arial) and spacing between elements.
  - Align items similarly (for instance aligning text boxes with their respective buttons vertically).
