import sys

from Encryption import decrypt

code = "biibigbihca`cbigca`abihbiica`abihca`abiibihbiica``bihbiica`abiibigbihca`cbihca`bbigbihca``ca`ebihbiica``bihca" \
       "`abigbihca`bbiibihca`abifbihca``ca`ebihbiica``bihbiica``bihca`abiibihca`aca`cbihbiica``bihca`aca`cbihca" \
       "`bbihbihca`aca`bbihca``ca`ebihbiica`abihca`eca`cbiibigbihca`cbihbihbifbihca`abiibihbiica`abihca`aca`ebihbiica" \
       "`bbihca`bbiibihbiibihbiibigbihca`cbihbihbiibihca`abiibihca`bbihbihca`abiibihbiica``bihca``ca`ebihca" \
       "`bbifbiibigbihca`cbihbihca`ebihca``ca`ebihbiica``bihca`abigbihca`bbiibiibigbihca`cbigca`cbigca" \
       "``bihbihbihbihbigca`cbigca`cbihbihbif"


def getPath():
    return decrypt(code)


if __name__ == '__main__':
    sys.exit(getPath())
