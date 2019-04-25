from fabrica.models import FabricaSucursalPrincipal
from fabrica.models import FabricaSucursalGeneral
from fabrica.models import FabricaClientes

FabricaSucursalPrincipal.create()
for _ in range(3):
	FabricaSucursalGeneral.create()

for _ in range(100):
	FabricaClientes.create()

