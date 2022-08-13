package generator

import (
    "fmt"
    "flag"
    "os"
    "math/rand"
    "strings"
)

var sizeFlag, numCitiesFlag int
var filenameFlag string


func main() {
    flag.IntVar(&sizeFlag, "n", 1, "Tamaño de la región")
    flag.IntVar(&numCitiesFlag, "m", 1, "Número de ciudades en la región.")
    flag.StringVar(&filenameFlag, "file","out.dzn", "Nombre de archivo de datos.")
    flag.Parse()

    fmt.Println("n ",sizeFlag)
    fmt.Println("m ",numCitiesFlag)

    file,err := os.Create(filenameFlag) 
    if err != nil {
	fmt.Println(err.Error())
	os.Exit(1)
    }
    defer file.Close()
    var content strings.Builder

    content.WriteString(fmt.Sprintf("n=%d;\nm=%d;\nciudades=[",sizeFlag, numCitiesFlag))

    for i:=0; i < numCitiesFlag; i++ {

	if i == numCitiesFlag -1 {
	    content.WriteString(fmt.Sprintf("|%d,%d|];",rand.Intn(sizeFlag),rand.Intn(sizeFlag)))
	} else {
	    content.WriteString(fmt.Sprintf("|%d,%d\n",rand.Intn(sizeFlag),rand.Intn(sizeFlag)))
	}
    }

    n,err := file.WriteString(content.String())
    if err != nil {
	fmt.Println(err.Error())
	os.Exit(1)
    }
    fmt.Printf("Wrote %d bytes to %v\n", n, filenameFlag)
}
