function Agregar-ReglasBloqueo{ 
	$puerto = Read-Host -Prompt "Cu�l puerto quieres bloquear?" 
	New-NetFirewallRule -DisplayName "Puerto-Entrada-$puerto" -Profile "Public" -Direction Inbound -Action Block -Protocol TCP -LocalPort $puerto 
}