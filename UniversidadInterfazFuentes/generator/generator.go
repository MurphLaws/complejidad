package main

import (
    "fmt"
    "flag"
    "os"
    "math/rand"
    "strings"
    "path/filepath"
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

    path, err := filepath.Abs("../../MisInstancias/"+filenameFlag)
    if err != nil {
	fmt.Println("Error", err.Error())
	os.Exit(1)
    }

    file,err := os.Create(path) 
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
