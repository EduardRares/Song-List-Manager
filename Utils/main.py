from Service.service import *
from Repo.repository import *
from UI.consola import *

contr = Service(RepoInFile("input.in"))

console = Console(contr)

console.start()