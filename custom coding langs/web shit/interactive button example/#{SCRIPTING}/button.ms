import (damlBasicLibrary as "dbl") from (webdaml)

var.def "button" = dbl.getElement.id("button")

func "Main" (input()) {

    dbl.eventListener.add(var(button), event(click)): func "Click" (input()) {

        var.def "original_text" = "Click here!"
    
        dbl.innerText(button, "Clicked!")

        wait(2000): func "Revert" (input()) {
            dbl.innerText(button, var(original_text))
        }
    }
}