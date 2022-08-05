package main

import (
	"C"
	"debug/buildinfo"
	"encoding/json"
	"errors"
	"fmt"
	"os"
	"path/filepath"
)

//export getgobuildinfo
func getgobuildinfo(fileNameIn *C.char) *C.char {
	return C.CString(getGoBuildInfoInternal(C.GoString(fileNameIn)))
}

func main() {
	//getgobuildinfo(C.CString("foo/bar"))
	//getgobuildinfo(C.CString("/usr/bin/du"))
	//getgobuildinfo(C.CString("/Users/mike/go/src/spire/support/oidc-discovery-provider/oidc-discovery-provider.elf"))
	//getgobuildinfo(C.CString("/Users/mike/go/src/spire/support/oidc-discovery-provider/oidc-discovery-provider.exe"))
	//getgobuildinfo(C.CString("/Users/mike/go/src/spire/support/oidc-discovery-provider/oidc-discovery-provider"))
}

func getGoBuildInfoInternal(fileName string) string {
	returnValue := "{ \"error\" : \"Unknown\" }"
	bi, err := buildinfo.ReadFile(fileName)
	if err != nil {
		if pathErr := (*os.PathError)(nil); errors.As(err, &pathErr) && filepath.Clean(pathErr.Path) == filepath.Clean(fileName) {
			returnValue = fmt.Sprintf("{ \"error\": \"path error:%v\" }", fileName)
		} else {
			returnValue = fmt.Sprintf("{ \"error\": \"%s: %v\"}", fileName, err)
		}
	} else {
		data, _ := json.Marshal(bi)
		returnValue = string(data)
		// bi.GoVersion = "" // suppress printing go version again
		// mod := bi.String()
		//if len(mod) > 0 {
		//	fmt.Printf("\t%s\n", strings.ReplaceAll(mod[:len(mod)-1], "\n", "\n\t"))
		//}
	}
	// fmt.Printf("%s\n", returnValue)
	return returnValue
}
