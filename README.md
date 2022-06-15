# dotfiles

My configuration files, managed by [chezmoi](https://www.chezmoi.io/).

One-liner to deploy all dotfiles on a fresh machine: `sh -c "$(curl -fsLS chezmoi.io/get)" -- init --apply jyannick`

To proceed with caution and check the changes before applying them:
- `sh -c "$(curl -fsLS chezmoi.io/get)" -- init jyannick`
- `chezmoi diff`
- if changes are ok: `chezmoi apply`