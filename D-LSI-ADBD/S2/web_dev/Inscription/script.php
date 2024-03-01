<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <style>
        body{
            display: flex;
            flex-direction: row;
            justify-content: center;
            align-items: center;
        }
        table{
            background-color: white;
            border-bottom-left-radius: 20px;
            border-bottom-right-radius: 20px;
            border: 1px solid rgb(41, 41, 41);
            width: 50%;
            text-align: left;
            padding: 0.5%;
        }
        table caption {
            padding: 1%;
            background-color:rgb(41, 41, 41);
            color: white;
            border-top-left-radius: 20px;
            border-top-right-radius: 20px;
        }
    </style>
    <title>Document</title>

</head>
<body>
<?php
    $prenom = isset($_POST["prenom"]) ? $_POST["prenom"] : "" ;
    $password = isset($_POST["password"]) ? $_POST["password"] : "" ;
    $association = isset($_POST["association"]) ? $_POST["association"] : "" ;
    $disponibilites = [] ;
    for ($i = 1; $i < 6; $i++){
        $key = "jour_".$i ;
        if (isset($_POST[$key]))
            array_push($disponibilites,$_POST[$key]) ;
    }

    $table = '
        <table class="result_table">
        <caption>Les information sur %s</caption>
        <tr>
            <th>Prénom : </th><td>%s</td>
        </tr>
        <tr>
            <th>Mot de passe : </th><td>%s</td>
        </tr>
        <tr>
            <th>Association : </th><td>%s</td>
        </tr>
        <tr>
            <th>Disponibilités pour la semaine du 22 juin : </th><td>%s</td>
        </tr>
        <tr>
            <th>Contribution : </th><td>%s</td>
        </tr>
        <tr>
            <th>Commentaires : </th><td>%s</td>
        </tr>
        </table>
    ' ;
    $contribution = isset($_POST["radio_input"]) ? $_POST["radio_input"] : "";
    $commentaire = isset($_POST["commentaire"]) ?  $_POST["commentaire"] : "";
    $disponibilites = ($disponibilites) ? join(", ", $disponibilites) : "" ;
    echo sprintf($table, $prenom, $prenom, $password, $association, $disponibilites, $contribution, $commentaire) ;
?>
</body>
</html>

