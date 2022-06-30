# Are We Game Yet

## What is this?

The Rust community has a number of websites dedicated to keeping track of the
state of the ecosystem for specific purposes. (e.g. [arewewebyet] and
[arewelearningyet])

This one tracks the state of the ecosystem for Game Development in Rust.

[arewewebyet]: https://www.arewewebyet.org
[arewelearningyet]: https://www.arewelearningyet.com

## Contribute

Arewegameyet? uses [semantic-ui](https://semantic-ui.com/), and
[zola](https://github.com/getzola/zola), the Rust static site generator. The
site currently builds with Zola 0.15.3. To get started with adding your own
project, you can do the following:

1. Navigate to whichever folder in `/content` best fits your project.
2. Edit that folder's `data.toml` file in any plain text editor or straight
   through [GitHub's editor][github-editor-docs].
3. Create a new entry, following the schema described below. Note that all
   entries should be sorted alphabetically by the `name` field, ignoring case.
   There is a CI check to ensure this is done correctly - you can use the
   `sort_data.py` script to automatically fix a file.

**All done!** We do greatly appreciate PRs, but if you're not comfortable with
this process, you're welcome to [open an issue][open-an-issue] requesting the addition of your
project instead.

[github-editor-docs]: https://help.github.com/articles/editing-files-in-another-user-s-repository/
[open-an-issue]: https://github.com/rust-gamedev/arewegameyet/issues/new/choose

### Schema

```toml
[[items]]
# The name of the item. Mandatory.
name = "My crate" 

# A short description of the item. Optional, but recommended.
description = "My extremely cool Rust crate" 

# The categories that your item should be assigned to. Mandatory.
categories = ["2drendering", "engines"]

# An image representing the item. Files should be checked in to
# /static/assets/img/, and the path should be absolute.
# Optional, but highly recommended for games!.
image = "/assets/img/logo.png"

# A link to the item's page on Crates.io. Optional.
crate_url = "https://crates.io/crates/mycrate"

# A link to the item's VCS repository. Optional.
repository_url = "https://github.com/username/repo"

# A link to the item's homepage. Optional.
homepage_url = "https://mycrate.com"

# A link to the item's Gitter chat. Optional.
gitter_url = "https://gitter.im/mycrate"
```

You can also tell the site to pull data directly from an external source:

```toml
[[items]]
# Pull data from Crates.io:
name = "mycratename"
source = "crates"
categories = ["mycategory"]

[[items]]
# Pull data from GitHub:
name = "username/repo"
source = "github"
categories = ["mycategory"]
```

Extra keys can be added to items that are pulled from external data (e.g. to add
a homepage URL, or override some of the fetched data).

### Enhance this website

If you're comfortable with semantic-ui and Zola please reach out to us in the
Issues with your enhancement ideas or just to state your willingness to
contribute.

[awgy-issues]: 

### Errors

It's very likely there are mistakes around, if you find one please file an
issue.

*Thanks for helping us map the Rust game development ecosystem!*
