# Description

Adding Creation of NFT asset functionality to
DEPENDENCIES: Crow and Pistache

The hashes for the Bazel build of dependencies were also outdated.

No documentation/readme for exposing an endpoint that had to be used for SDK.

## Fixes # (issue)

1. Uncommenting the code at:
   <https://github.com/msadoghi/nexres/blob/master/WORKSPACE#L195>
   <https://github.com/msadoghi/nexres/blob/master/third_party/BUILD#L73>
   <https://github.com/msadoghi/nexres/blob/master/sdk_client/BUILD#L7>

2. Updating hashes at:
   <https://github.com/msadoghi/nexres/blob/9289e91bccea9bcfcd36463c46c6717ce573b90a/WORKSPACE#L207>
   <https://github.com/msadoghi/nexres/blob/9289e91bccea9bcfcd36463c46c6717ce573b90a/WORKSPACE#L222>

3. Adding [readme.md](https://github.com/msadoghi/nexres/blob/54e936cbbea9259a284ae10bdc5cc912c456b495/sdk_client/README.md) to /nexres/sdk_client for local and remote development.
   https://github.com/msadoghi/nexres/blob/54e936cbbea9259a284ae10bdc5cc912c456b495/sdk_client/README.md

## Type of change

- [x] Bug fix (non-breaking change which fixes an issue)
      Please check the hashes and workspace.

- [x] This change requires a documentation update
      This has been made at sdk_client/README.md

## Possible Breaks

1. PyLance is generating a warning for an Undefined Variable

# How Has This Been Tested?

Using instructions in /nexres/sdk_client/README.md, I have tested with a clean repo.

- [x] Test A
      Using CREATE method from nexres_sdk
- [x] Test B
      Setup NexresDB server on OCI Kaustubh-Dev

I did not find any unit tests on the repo. So I have tested on the local system as well as OCI. Please re-verify the build files so that I don't make a security compromise.

**Test Configuration**:
**Local Environment overview**

- Environment Location: Ubuntu LTS 20.04
- System Config: Acer Aspire 5 i7 16GB 512 HDD (Ubuntu Running on External HDD)
- Method of repo install: git clone
- Python Env Manager: conda

**Remote Environment overview**

- Environment Location: OCI Kaustubh Dev Instance Ubuntu LTS 20.02
- System Config: VM.Standard.E2.8
- Image: hyper_ledger_tcp
- Method of repo install: git clone
- Dev Env Manager: conda
- Firmware: UEFI_64
- FQDN: kaustubh-dev-656015.subnet08231419.vcn08231419.oraclevcn.com

## Suggestions

Some information about /nexres/sdk_client/README.md should be included at main /nexres/README.md when we roll out the v0.1 for nexres_sdk

# Checklist

- [x] My code follows the style guidelines of this project
- [x] I have performed a self-review of my own code
- [x] I have commented on my code, particularly in hard-to-understand areas
- [x] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [x] I have added tests that prove my fix is effective or that my feature works
- [x] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published in downstream modules
