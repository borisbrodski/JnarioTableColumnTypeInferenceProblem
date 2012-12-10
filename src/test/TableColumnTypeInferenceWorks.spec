package test


describe "Tests type inference of the table columns"{
	def myTable {
		| value          |
		| MyEnum::VALUE1 |
		| MyEnum::VALUE2 |
    }		
	
	fact "Table column type get inferred by the stand-alone compile correctly" {
		myTable.forEach [
			acceptPruefungsArt(value)
		]
	}
	
	def acceptPruefungsArt(MyEnum myEnum) {
		
	}
}