<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        function createTable($name) {
            $etudiants=[
                "ali"=>["html"=>[12,15,14],"java"=>[10,18,13],"angular"=>[14,13.5,17]],
                "mohamed"=>["html"=>[13,18,15],"java"=>[9,7,3],"angular"=>[8,7.5,7]],
                "sami"=>["html"=>[17,18,20],"java"=>[14,18,15.5],"angular"=>[13,17.5,18]],
            ];
            $table = '
                <h2>%s</h2>
                <table border="1">
                 <tr>
                  <th>matiere</th><th>note tp</th><th>note ds</th><th>note examen</th><th>moyenne</th>
                 </tr>
                  %s
                 <tr>
                  <td colspan="4">Moyenne generale</td><td>%s</td>
                 </tr>
                 <tr>
                  <td colspan="4">Mention</td><td>%s</td>
                 </tr>
                </table>
            ' ;
            
            $moyenne_generale = 0 ;
    
            $table_row = '' ;
            foreach ($etudiants[$name] as $matiere => $row){
                $row_moyenne = array_sum($row) / 4 ;
                $table_row .= sprintf("
                <tr>
                 <td>%s</td><td>%s</td><td>%s</td><td>%s</td><td>%s</td>
                </tr>
                ", $matiere, $row[0], $row[1], $row[2], round($row_moyenne, 2)) ;
    
                $moyenne_generale+=round($row_moyenne, 2) ;
            }
            $moyenne_generale/=3 ;
            
            $mention = "" ;
            switch($moyenne_generale) {
                case $moyenne_generale < 10 :
                    $mention = "refusé" ;
                    break ;
                case $moyenne_generale < 12 :
                    $mention = "assez bien" ;
                    break ;
                case $moyenne_generale < 14 :
                    $mention = "bien" ;
                    break ;
                default :
                    $mention = "trés bien" ;
                    break ;
            }
    
            echo sprintf($table, $name, $table_row, round($moyenne_generale,2), $mention) ;
        }
        createTable("mohamed") ;
    ?>
</body>
</html>
