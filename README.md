### Basic Preliminaries

- Ask a team member to add you to the CSSAT organization in GitHub. 

- Ask a team member to add you to the CSSAT vault in 1Pass. 

- Ensure that you have postgres installed and running on your machine. 

- Ensure that you have a recent-ish version of node, yarn, and npm on your machine. 

### Github Packages Authentication

- Generate personal access token through [Github](https://github.com/settings/tokens)
- Add the following lines to `~/.npmrc`
    ```text
    //npm.pkg.github.com/:_authToken=<PERSONAL_ACCESS_TOKEN>
    //npm.pkg.github.com/cssat/:_authToken=<PERSONAL_ACCESS_TOKEN>
    ```
- `yarn login --registry=https://npm.pkg.github.com`
    * Enter your **Github username**
    * Enter your **email address** associated with your Github account

- Make sure that your [SSH key(s) are added to your GitHub account](https://docs.github.com/en/github/authenticating-to-github/connecting-to-github-with-ssh). 

### Clone Required Repos

- Run `script/clone-repos-list.sh referral-repo.list` to download the repos required to completely establish a development referral environment (WARNING: This script will `rm -R -f` any directory with the prefix `acorn-` before beginning the clone). Repos will clone into the directory that the script is run from.

### Cleanup & Setup Required Repos

- Find `script/dev-setup` in all repos. Ensure that `YARN_VERSION=X.X.X` is set for the version of yarn you are running. If it's not, update the yarn version to match `yarn -v` (TODO: update yarn version check to be "greater than" X instead of "equal to" X). 

- Run `script/setup-install-build.sh`. This should complete all of the relevant setup commands across the cloned repos. If needed, the script will also start databases across the repos. When prompted, enter the Transcrypt password from the CSSAT vault within the Substantial 1Password account. 

- If you don't have an email address with the `substantial.com` domain, ask a CSSAT team member to be added to the Google Developer `esit-migrate-project`. There, you will find the `OIDC_CLIENT_ID` and `OIDC_CLIENT_SECRET` for the `esit-migrate-web-client`. Next, in `acorn-api/api/.envrc`...
    * Comment the `OIDC_CLIENT_ID` and `OIDC_CLIENT_SECRET` variables you just decrypted above. 
    * Replace the commented variables with `OIDC_CLIENT_ID` and `OIDC_CLIENT_SECRET` from the `esit-migrate-web-client`
(TODO: We should probably just finish SAW integration so we can all run from a single client id and secret)

### Host or Start the Repos

- Start the api:
    ```text
    cd acorn-api/api
    yarn host
    ```
- Start the web client:
    ```text
    cd acorn-web-client
    yarn start
    ```
    NOTE: It may also be helpful to add an `.env.local` to `acorn-web-client` with a `SKIP_PREFLIGHT_CHECK=true` entry. See further discussion [here](https://stackoverflow.com/questions/52606707/cannot-uninstall-webpack-from-react-script).
    
- Start the referral component:
    ```text
    cd acorn-referral-component/component
    yarn host
    ```
- Start the referral viewdata:
    ```text
    cd acorn-referral-viewdata
    yarn host
    ```

### Connect to AWS MSSQL

- Until we set up ssh tunneling, ssh into the box
    ```text
    ssh ec2-user@ec2-34-234-208-52.compute-1.amazonaws.com
    ```
- optionally:
    ```text
    ssh -i <path-to-private-key> ec2-user@ec2-34-234-208-52.compute-1.amazonaws.com
    ```

- connect to the mssql db
    ```text
    sqlcmd -S cssat-dcyf-db.crartr7yq7ee.us-east-1.rds.amazonaws.com,1433 -U admin -P <password>
    ```
