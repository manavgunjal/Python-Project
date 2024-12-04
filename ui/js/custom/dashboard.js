$(function () {
    // Json data by API call for order table
    $.get(orderListApiUrl, function (response) {
        if (response) {
            let table = '';
            let totalCost = 0;

            $.each(response, function(index, order) {
                let totalValue = 0.00;

                // Assuming order is an array: [id, customer_name, total, datetime]
                if (Array.isArray(order) && order.length >= 4) {
                    const totalFromArray = order[2]; // Total is the third element
                    totalValue = parseFloat(totalFromArray); // Convert the string to a number

                    // Check if totalValue is valid
                    if (isNaN(totalValue)) {
                        console.error("Invalid 'total' value for order:", order);
                        return; // Skip this order if total is invalid
                    }

                    // Only add to totalCost if totalValue is valid
                    if (totalValue > 0) {
                        totalCost += totalValue;
                    }

                    table += `<tr>
                                <td>${order[3] || ''}</td> <!-- datetime -->
                                <td>${order[0] || ''}</td> <!-- order_id -->
                                <td>${order[1] || ''}</td> <!-- customer_name -->
                                <td>${totalValue.toFixed(2)} Rs</td>
                            </tr>`;
                } else {
                    console.error("Invalid order format:", order);
                }
            });

            table += `<tr><td colspan="3" style="text-align: end"><b>Total</b></td><td><b>${totalCost.toFixed(2)} Rs</b></td></tr>`;
            $("table").find('tbody').empty().html(table);
        }
    });
});