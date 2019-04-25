from fabrica.models import FabricaSucursalPrincipal
from fabrica.models import FabricaSucursalGeneral

FabricaSucursalPrincipal.create()
for _ in range(3):
	FabricaSucursalGeneral.create()

