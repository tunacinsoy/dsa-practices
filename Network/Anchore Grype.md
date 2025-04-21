
> [!NOTE] What is Anchore Grype?
> Anchore Grype (https://github.com/anchore/grype) is a container vulnerability scanner that scans your images for known vulnerabilities and reports their severity. Based on that, you can take appropriate actions to prevent vulnerabilities by including a different base image or modifying the layers to remove vulnerable components.
> 

```bash
# Install grype locally
curl -sSfL https://raw.githubusercontent.com/anchore/grype/main/install.sh -o install.sh
sudo sh install.sh -b /usr/local/bin
```
---
```bash 
# Scan an image for vulnerability. This will report a list of vulnerabilities with severities `Negligible, Low, Medium, High, Critical, Unknown`  within the image.
grype <image_name>
```
---
```bash
# If we don’t want to allow any Critical vulnerabilities in the container, we can use this. 
grype -f critical <container-image>
```
---
