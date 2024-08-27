document.addEventListener('DOMContentLoaded', function() {
    const logTypes = ['application', 'system', 'security'];
    logTypes.forEach(type => {
        fetch(`/logs/${type}`)
            .then(response => response.json())
            .then(data => {
                if (data.length > 0) {
                    populateTable(type, data);
                    updateChart(type, data);
                } else {
                    console.warn(`No logs available for ${type}`);
                    document.querySelector(`#${type}-log-table tbody`).innerHTML = '<tr><td colspan="5">No logs available</td></tr>';
                }
            })
            .catch(error => console.error('Error fetching logs:', error));
    });
});

function populateTable(type, data) {
    const tableBody = document.querySelector(`#${type}-log-table tbody`);
    
    if (!tableBody) {
        console.error(`Table body with ID ${type}-log-table tbody not found`);
        return;
    }

    tableBody.innerHTML = '';
    
    data.forEach(log => {
        const row = document.createElement('tr');
        row.innerHTML = `
            <td>${log.timestamp || 'N/A'}</td>
            <td>${log.event_id || 'N/A'}</td>
            <td>${log.source || 'N/A'}</td>
            <td>${log.category || 'N/A'}</td>
            <td>${log.description || 'No description'}</td>
        `;
        tableBody.appendChild(row);
    });
}

function updateChart(type, data) {
    const ctx = document.getElementById(`${type}-severity-chart`);
    
    if (!ctx) {
        console.error(`Canvas with ID ${type}-severity-chart not found`);
        return;
    }

    const chartContext = ctx.getContext('2d');
    const severities = data.reduce((acc, log) => {
        const severity = log.severity || 'Unknown';
        acc[severity] = (acc[severity] || 0) + 1;
        return acc;
    }, {});

    new Chart(chartContext, {
        type: 'pie',
        data: {
            labels: Object.keys(severities),
            datasets: [{
                data: Object.values(severities),
                backgroundColor: [
                    '#ff6384', // red
                    '#36a2eb', // blue
                    '#cc65fe', // purple
                    '#ffce56', // yellow
                    '#e7e9ed'  // light gray for unknown
                ]
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                tooltip: {
                    callbacks: {
                        label: function(tooltipItem) {
                            const label = tooltipItem.label || '';
                            const value = tooltipItem.raw || 0;
                            return `${label}: ${value}`;
                        }
                    }
                }
            }
        }
    });
}
