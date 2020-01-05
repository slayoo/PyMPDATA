class Options:
    def __init__(self,
                 nug: bool = False,
                 iga: bool = False,
                 fct: bool = False,
                 dfl: bool = False,
                 tot: bool = False,
                 eps: float = 1e-8,
                 mu: float = 0
                 ):
        self._nug = nug
        self._iga = iga
        self._fct = fct
        self._dfl = dfl
        self._tot = tot
        self._eps = eps
        self._mu = mu

    @property
    def nug(self) -> bool:
        return self._nug

    @property
    def iga(self) -> bool:
        return self._iga

    @property
    def fct(self) -> bool:
        return self._fct

    @property
    def dfl(self) -> bool:
        return self._dfl

    @property
    def tot(self) -> bool:
        return self._tot

    @property
    def eps(self) -> float:
        return self._eps

    # for definition of mu (mesh Fourier number),
    # see eq. 20 in Sousa 2009, doi:10.1002/fld.1984
    @property
    def mu(self) -> float:
        return self._mu
