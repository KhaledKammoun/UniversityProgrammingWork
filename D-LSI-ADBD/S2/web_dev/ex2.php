<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <?php
        // Check if form is submitted
        if ($_SERVER["REQUEST_METHOD"] == "POST") {
            // If form submitted, change the value of $main
            $main = "Name 1";
        } else {
            // Initial value of $main
            $main = "Name 2";
        }
    ?>

    <h1><?php echo $main; ?></h1>
    
    <form method="post" action="<?php echo $_SERVER['PHP_SELF']; ?>">
        <button type="submit">Change Name</button>
    </form>
</body>
</html>
