$(function () {

    // pick color input
        let colorPicker = $('#colorPicker');
    // choose size input
        const height = $('#input_height'), width = $('#input_width');
    // create canvas
        const canvas = $('#pixel_canvas');


    // When size is given as the input then call the function makeGrid()
        function makeGrid() {
            // remove any tbody if already present
            canvas.find('tbody').remove(); /*This is to prevent adding
            on to the table rows and column if submitted multiple times*/

            // submitting the form to create the input size table
            const gridRow = height.val(), gridColm = width.val();

            // append tbody in the table
            canvas.append('<tbody></tbody>');


            let table = canvas.find('tbody');

            // create row of the table
            for (let i = 0; i < gridRow; i++) {
                table.append('<tr></tr>');
            }

            // create column associated with each row
            for (let i = 0; i < gridColm; i++) {
                canvas.find('tr').append('<td class="transparent"></td>');
            }

        }

        // toggle table color
        $('#pixel_canvas').on('click', 'td', function (e) {
            let chosencolor = colorPicker.val();
            let existingColor = $(this).css('background-color');
            console.log(existingColor+ " color:" + chosencolor);
            if ($(this).hasClass('transparent')){
                $(this).toggleClass('transparent');
                $(this).css("background-color", chosencolor);
            } else{
                $(this).toggleClass('transparent');
                $(this).css("background-color", "transparent");
            }

        })

        $(document).ready(function () {
            // press on submit button to create or update the table
            $('input[type="submit"]').on('click', function (e) {
                e.preventDefault();
                makeGrid();
            });

        });

    });
