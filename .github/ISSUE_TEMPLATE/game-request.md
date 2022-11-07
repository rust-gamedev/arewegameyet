---
name: Request a game addition
about: Ask for a game to be added to Are We Game Yet
title: ''
labels: addition, good first issue
assignees: ''

---

Fill out as many of the fields as you can, and remove any that you don't need:

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
