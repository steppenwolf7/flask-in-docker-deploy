Flask App Deployment (Rocky Linux)

This project demonstrates a simple workflow for deploying a Flask application to a Rocky Linux server using Git.

🚀 Deployment Workflow

For now, deployment is done by pushing changes directly from the local development environment to the Rocky Linux server using Git.

How it works

Local development

You develop and test the Flask app on your local machine.

Changes are committed to the local Git repository.

Push to remote repository

The project is pushed to a GitHub repository:

git push origin main

Pull on the Rocky Linux server

On the Rocky Linux server, the same repository is cloned.

The server pulls the latest changes:

git pull origin main

Restart the application (if needed)

After pulling updates, the Flask app or related services (e.g. Gunicorn, Docker, systemd) are restarted so changes take effect.

🧱 Current State

No CI/CD pipeline yet

No automated builds or deployments

All updates are manual via Git push/pull

🔮 Future Improvements

Planned enhancements:

Add a CI/CD pipeline (e.g. GitHub Actions)

Automatic deployment on push

Docker image build & push

Zero-downtime restarts
