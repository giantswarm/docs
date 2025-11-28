# Improve the writing style and formatting of modified/added pages

1. Check via git tools which changes the user has made so far. Only treat the pages and content sections the user has added/modified. Alternatively, if a path has been passed to the command, treat that file.

2. Fix any obvious grammar problems. When in doubt, explain a grammar problem to the user and let the user fix the problem.

3. Run `vale` validation as shown in the `lint-prose` target in `Makefile`, but only for modified/added pages, not for the entire content directory. This is the rough syntax:

   ```
   docker run --rm -ti \
     -v $PWD:/workdir -w /workdir \
     <vale-container-image> \
     --config=/workdir/.vale.ini \
     --no-wrap \
     <relative-path-to-markdown-file>
   ```

4. Mitigate the vale complaints.

IMPORTANT: When making changes to the content, make sure to not modify the meaning of the content, or remove any detail!
