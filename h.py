
def draaw_circle(diametr_of_duct,distance_between_duct,bountary_dist ):
    style = """<style>
            .box {
                width: 500px;  /* Width of the box */
                height: 250px; /* Height of the box */
                border: 2px solid black; /* Box outline */
                display: flex; /* Use flexbox for alignment */
                justify-content: center; /* Center horizontally */
                align-items: center; /* Center vertically */
                position: relative; /* Positioning context for circles */
            }

            .circle {
                width: 80px;  /* Diameter of the circles */
                height: 80px; /* Diameter of the circles */
                border: 5px solid rgb(10, 10, 10); /* Circle outline color and thickness */
                border-radius: 50%; /* Makes the div circular */
                background-color: transparent; /* No fill color */
                position: absolute; /* Positioning circles absolutely */
            }

            .circle1 {
                top: 50%; /* Center vertically */
                left: 30%; /* Position the first circle */
                transform: translate(-50%, -50%); /* Center the circle */
            }

            .circle2 {
                top: 50%; /* Center vertically */
                left: 70%; /* Position the second circle */
                transform: translate(-50%, -50%); /* Center the circle */
            }

            svg {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
            }

            text {
                font-family: Arial, sans-serif;
                font-size: 12px;
                fill: black; /* Text color */
            }
        </style>"""

    html= f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Two Circles with Lines and Lengths</title>
        {style}
    </head>
    <body>
        <div class="box">
            <div class="circle circle1"></div>
            <div class="circle circle2"></div>
            <svg>
                <!-- Line from border to center of Circle A -->
                <line x1="0" y1="125" x2="105" y2="125" stroke="red" stroke-width="4" />
                <text x="45" y="140" text-anchor="middle">Length: {bountary_dist}</text> <!-- Length of the first line -->
                
                <line x1="105" y1="125" x2="190" y2="125" stroke="black" stroke-width="4" />
                <text x="155" y="140" text-anchor="middle"> {diametr_of_duct}</text> <!-- Length of the second line -->

                <!-- Line from center of Circle A to center of Circle B -->
                <line x1="195" y1="125" x2="305" y2="125" stroke="green" stroke-width="4" />
                <text x="250" y="140" text-anchor="middle">Length: {distance_between_duct}</text> <!-- Length of the second line -->

                <!-- Line from center of Circle A to center of Circle B -->
                <line x1="305" y1="125" x2="390" y2="125" stroke="black" stroke-width="4" />
                <text x="350" y="140" text-anchor="middle"> {diametr_of_duct}</text> <!-- Length of the second line -->

                <!-- Line from center of Circle B to border -->
                <line x1="395" y1="125" x2="500" y2="125" stroke="red" stroke-width="4" />
                <text x="450" y="140" text-anchor="middle">Length: {bountary_dist}</text> <!-- Length of the third line -->
            </svg>
        </div>
    </body>
    </html>"""

    return html