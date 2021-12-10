$(function () {
    $('.toggle-menu').click(function(){
        $('.exo-menu').toggleClass('display');
    });
});

    const slider = $("#calculatorSlider");
        const developerBtn = $("#developerBtn");
        const corporateBtn = $("#corporateBtn");
        const privateBtn = $("#privateBtn");
        const reseller = $("#resellerEarnings");
        const client = $("#clientPrice");
        const percentageBonus = 30; // = 30%
        const license = {
            corpo: {
                active: true,
                price: 319,
            },
            dev: {
                active: false,
                price: 149,
            },
            priv: {
                active: false,
                price: 79,
            }
        }

        function calculate(price, value) {
            client.text((Math.round((price - (value / 100 * price)))) + '$');
            reseller.text((Math.round(((percentageBonus - value) / 100 * price))) + '$')
        }

        function reset(price) {
            slider.val(0);
            client.text(price + '$');
            reseller.text((Math.round((percentageBonus / 100 * price))) + '$');
        }
        developerBtn.on('click', function (e) {
            license.dev.active = true;
            license.corpo.active = false;
            license.priv.active = false;
            reset(license.dev.price)
        });
        privateBtn.on('click', function (e) {
            license.dev.active = false;
            license.corpo.active = false;
            license.priv.active = true;
            reset(license.priv.price);
        });
        corporateBtn.on('click', function (e) {
            license.dev.active = false;
            license.corpo.active = true;
            license.priv.active = false;
            reset(license.corpo.price);
        });
        slider.on("input change", function (e) {
            if (license.priv.active) {
                calculate(license.priv.price, $(this).val());
            } else if (license.corpo.active) {
                calculate(license.corpo.price, $(this).val());
            } else if (license.dev.active) {
                calculate(license.dev.price, $(this).val());
            }
        })

        $('#calculatorSlider').demo({
            width: '25%',
            single: {
                active: true,
                multi: {
                    active: true,
                    rangeLength: 1
                },
            }
        });



