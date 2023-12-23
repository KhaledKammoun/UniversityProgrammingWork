function age(){

        var input = document.getElementById('input_date').value;
        var tab = input.split('/');

        if (tab.length === 3) {
            var mois = parseInt(tab[1]) ;
            var annee = parseInt(tab[2]);

            var currentDate = new Date();
            var age = currentDate.getFullYear() - annee ;
            document.querySelector('#result h2').innerHTML = `vous étes né au mois : ${mois} de l'année : ${annee}<br>
            Votre Age=${age}`
        } else {
            document.querySelector('#result h2').innerHTML = 'Taper votre date de naissance(jj/mm/aaaa) !!';
        }
}