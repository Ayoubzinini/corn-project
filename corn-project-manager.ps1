$act=0
while ($act -eq 0) {
	cd E:\scripts\corn-project
	"0 : Modify"
	"1 : Run"
	$dir = get-childitem
		$pyfiles = @()
		foreach ($file in $dir){
			if ($file.fullname.ToString() -like "*.py") {
				$pyfiles += $file.fullName.ToString()
			}
		}
	$m_or_r= Read-Host -Prompt "Modify or Run?"
	if ($m_or_r -eq 0){
		"0 : A lot of files"
		"1 : One file"
		$l_or_o= Read-Host -Prompt "A lot of files or one file?"
		if ($l_or_o -eq 0){
			code .
		}
		elseif ($l_or_o -eq 1) {
			$i = 0
			foreach ($file in $pyfiles){
				$i.ToString() + " : " + $file.ToString().substring(24)
				$i += 1
			}
			$choosed = Read-Host -Prompt "Choose the index of the target file to run it"
			code $pyfiles[$choosed].substring(24)
		}
	}
	elseif ($m_or_r -eq 1){
		"Your python files : "
		$i = 0
		foreach ($file in $pyfiles){
			$i.ToString() + " : " + $file.ToString().substring(24)
			$i += 1
		}
		$choosed = Read-Host -Prompt "Choose the index of the target file to run it"
		python $pyfiles[$choosed].substring(24)
	}
	$act = Read-Host -Prompt "Input 0 to continue or another value to go out"
}
