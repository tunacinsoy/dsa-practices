
> [!NOTE] What is GitHub Actions?
> **Note**: A GitHub Actions workflow is a simple YAML file that contains the build steps. We must create this workflow in the `.github/workflows` directory within the repository. Versioning can be achieved by the following `build.yaml` file.
> ```yaml
> name: Build and Test App
> on:
>   push:
>     branches: [main]
>   pull_request:
>     branches: [main]
> jobs:
>   build:
>     runs-on: ubuntu-latest
>     steps:
>       - uses: actions/checkout@v2
>       - name: Read version from file
>         id: vars
>         run: |
>           VERSION=$(cat version.txt)
>           TIMESTAMP=$(date +'%Y%m%d%H%M%S')
>           COMMIT_HASH=$(git rev-parse --short "$GITHUB_SHA")
>           echo "VERSION=${VERSION}" >> $GITHUB_ENV
>           echo "TIMESTAMP=${TIMESTAMP}" >> $GITHUB_ENV
>           echo "COMMIT_HASH=${COMMIT_HASH}" >> $GITHUB_ENV
>       - name: Login to Docker Hub
>         run: docker login -u ${{ secrets.DOCKER_USER }} -p ${{ secrets.DOCKER_PASSWORD }}
>       - name: Build the Docker image
>         run: docker build . --file Dockerfile --tag ${{ secrets.DOCKER_USER }}/sba-posts:${{ env.VERSION }}-${{ env.TIMESTAMP }}-${{ env.COMMIT_HASH }}
>       - name: Push the Docker image
>         run: docker push ${{ secrets.DOCKER_USER }}/sba-posts:${{ env.VERSION }}-${{ env.TIMESTAMP }}-${{ env.COMMIT_HASH }}
> 
> 
> ### Output image name: tunacinsoy/sba-posts:v1.0.0-2024.07.21.14.12-32a70ab
> ```
> 
> 