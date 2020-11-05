<h1 class="aches">AirBnB_clone</h1>
<img src="https://holbertonintranet.s3.amazonaws.com/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUWMNL5ANN%2F20201104%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20201104T191831Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=dbff06371251b417d52dca1fdc460a4f121fd0062e5eaf561e52e3d227991fe1"><br>
Para esta primera parte del proyecto se ha creado un interprete de comandos utilizando el lenguaje de programacion Python con el fin de poder gestionar nuestros objetos.

<h4 class="aches">Pa que sirve</h4>
<p>Con esta consola podremos crear, ver, eliminar y actualizar objetos los objetos estaran guardados en un archivo json para garantizar la persistencia de estos mismos en cada ejecucion del programa</p>

<h4 class="aches">Requisitos y como utilizar</h4>
<ol>Tener instalado Python. (preferiblemente la version 3) </ol>
<ol>1. Ejecutar el archivo "console.py" para entrar a la consola</ol>
<ol><pre class="show_code">
$ ./console
(hbnb)
</pre></ol>
<ul>Comandos
<li>Create</li>
<ol><pre class="show_code">
(hbnb) create <span class="resalto">BaseModel</span>       ->   Create a object. syntax : create "class name"
</pre></ol>
<li>Show</li>
<ol><pre class="show_code">
(hbnb) show <span class="resalto">BaseModel</span> <span class="resalto2">49faff9a-6318-451f-87b6-910505c55907 </span>     ->   show all the info of the object by the class name and ID. syntax : show "class name" "ID"
</pre></ol>
<li>All</li>
<ol><pre class="show_code">
(hbnb) all <span class="resalto">BaseModel</span>      ->   show all the info of the object class name. syntax : all "class name"
</pre></ol>
<li>Update</li>
<ol><pre class="show_code">
(hbnb) update <span class="resalto">BaseModel</span> <span class="resalto2">49faff9a-6318-451f-87b6-910505c55907 </span><span class="resalto3"> first_name "Betty"</span>    ->   update the object by adding a new atribbute and value of this. syntax : update "class name" "ID" "attribute" "attribute value"
</pre></ol>
<li>Destroy</li>
<ol><pre class="show_code">
(hbnb) destroy <span class="resalto">BaseModel</span> <span class="resalto2">49faff9a-6318-451f-87b6-910505c55907 </span>     ->   destroy all the info of the object by. syntax : destroy "class name" "ID"
</pre></ol>
<li>Help</li>
<ol><pre class="show_code">
(hbnb) <span class="resalto">help</span> <span class="resalto2">create </span>     ->   display info about the command. syntax : help "command"
</pre></ol>
<li>Quit</li>
<ol><pre class="show_code">
(hbnb) <span class="resalto">quit</span> or <span class="resalto2">EOF </span>     ->   exit the program.
</ul>


<h3 class="aches">Made by</h3>
<span class="names">Francisco Guzmán</span> - Twitter <a href="https://twitter.com/I7RANKI"> @I7RANKI
 </a> - Github <a href="https://github.com/I7RANK"> I7RANKI </a><br>
<span class="names">Mauricio Contreras</span> - Twitter <a href="https://twitter.com/MauroJCF"> @MauroJCF </a> - Github <a href="https://github.com/mauroxcf"> mauroxcf </a>

<style>
    * {
        background: #1b1b1b;
        font-family: Calibri;
        font-size: 14pt;
        color: #ccc;
    }

    .aches {
        color: #f0483e;
    }

    .show_code {
        background: #222222;
        box-shadow: inset 0 0 5px #000;
        margin: 0;
    }

    .resalto {
        background: transparent;
        color: cyan;
    }

    .resalto2 {
        background: transparent;
        color: green;
    }

    .resalto3 {
        background: transparent;
        color: orange;
    }
    .names {
        animation: change_color 1s infinite ease-in;
    }

    @keyframes change_color {
        0% {color: #fff;}
        50% {color: #f0483e;}
        100% {color: #fff;}
    }
</style>

















