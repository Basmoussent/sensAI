# Installation GitHub CLI sur Fedora 41

## Méthode 1 : DNF (Recommandée)

```bash
# Installer GitHub CLI
sudo dnf install gh

# Vérifier l'installation
gh --version

# Authentification
gh auth login
```

## Méthode 2 : Via script officiel

```bash
# Télécharger et installer
curl -fsSL https://cli.github.com/packages/rpm/gh-cli.repo | sudo tee /etc/yum.repos.d/gh-cli.repo
sudo dnf install gh -y

# Vérifier
gh --version

# Authentification
gh auth login
```

## Configuration après installation

```bash
# 1. Se connecter (choisir HTTPS et browser auth)
gh auth login

# 2. Configurer git
gh auth setup-git

# 3. Tester la connexion
gh auth status

# 4. Vérifier l'accès au repo
gh repo view
```

## Commandes utiles

```bash
# Créer des issues
gh issue create --title "Title" --body "Description"

# Voir les issues
gh issue list

# Créer un project
gh project create --title "sensAI Project" --owner @me

# Voir les projects
gh project list --owner @me
```
