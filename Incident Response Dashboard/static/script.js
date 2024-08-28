document.addEventListener('DOMContentLoaded', function() {
    // Show loading indicator
    const loadingMessage = document.getElementById('loading-message');
    loadingMessage.style.display = 'block'; // Show loading message

    // Fetch and display incidents
    fetch('/incidents')
        .then(response => response.json())
        .then(incidents => {
            loadingMessage.style.display = 'none'; // Hide loading message
            if (incidents.length > 0) {
                populateIncidentTable(incidents);
            } else {
                console.warn('No incidents available');
                document.querySelector('#incident-table tbody').innerHTML = '<tr><td colspan="8" class="error">No incidents available</td></tr>';
            }
        })
        .catch(error => {
            console.error('Error fetching incidents:', error);
            document.querySelector('#incident-table tbody').innerHTML = '<tr><td colspan="8" class="error">Failed to load incidents. Please try again later.</td></tr>';
        });

    // Fetch and display playbook steps
    fetch('/playbook-steps')
        .then(response => response.json())
        .then(steps => {
            if (steps.length > 0) {
                populatePlaybookSteps(steps);
            } else {
                console.warn('No playbook steps available');
                document.querySelector('#playbook-steps-list').innerHTML = '<li>No playbook steps available</li>';
            }
        })
        .catch(error => {
            console.error('Error fetching playbook steps:', error);
            document.querySelector('#playbook-steps-list').innerHTML = '<li>Failed to load playbook steps. Please try again later.</li>';
        });

    // Fetch and display system health, active alerts, incident summary, and recent activities
    fetch('/system-health')
        .then(response => response.json())
        .then(data => {
            if (data) {
                document.getElementById('system-health').innerHTML = `<h3>System Health</h3><p>CPU Usage: ${data.cpuUsage}</p><p>Memory Usage: ${data.memoryUsage}</p><p>Disk Space: ${data.diskSpace}</p>`;
            }
        })
        .catch(error => console.error('Error fetching system health data:', error));

    fetch('/active-alerts')
        .then(response => response.json())
        .then(data => {
            if (data.length > 0) {
                populateActiveAlerts(data);
            } else {
                document.getElementById('active-alerts').innerHTML = '<h3>Active Alerts</h3><p>No active alerts</p>';
            }
        })
        .catch(error => console.error('Error fetching active alerts:', error));

    fetch('/incident-summary')
        .then(response => response.json())
        .then(data => {
            if (data) {
                document.getElementById('incident-summary').innerHTML = `<h3>Incident Summary</h3><p>Total Incidents: ${data.totalIncidents}</p><p>Open Incidents: ${data.openIncidents}</p><p>Closed Incidents: ${data.closedIncidents}</p>`;
            }
        })
        .catch(error => console.error('Error fetching incident summary:', error));

    fetch('/recent-activities')
        .then(response => response.json())
        .then(data => {
            if (data.length > 0) {
                populateRecentActivities(data);
            } else {
                document.getElementById('recent-activities').innerHTML = '<h3>Recent Activities</h3><p>No recent activities</p>';
            }
        })
        .catch(error => console.error('Error fetching recent activities:', error));

    // Function to populate incident table
    function populateIncidentTable(incidents) {
        const tableBody = document.querySelector('#incident-table tbody');
        tableBody.innerHTML = '';

        incidents.forEach(incident => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${incident.id}</td>
                <td>${incident.name}</td>
                <td>${incident.status}</td>
                <td>${incident.priority}</td>
                <td>${incident.timestamp}</td>
                <td>${incident.source}</td>
                <td>${incident.message}</td>
                <td><button onclick="viewIncidentDetails(${incident.id})">View</button></td>
            `;
            tableBody.appendChild(row);
        });
    }

    // Function to populate playbook steps
    function populatePlaybookSteps(steps) {
        const stepsList = document.querySelector('#playbook-steps-list');
        stepsList.innerHTML = '';

        steps.forEach(step => {
            const listItem = document.createElement('li');
            listItem.textContent = step.description;
            stepsList.appendChild(listItem);
        });
    }

    // Function to populate active alerts
    function populateActiveAlerts(alerts) {
        const alertsContainer = document.getElementById('active-alerts');
        alertsContainer.innerHTML = '<h3>Active Alerts</h3><ul>' + alerts.map(alert => `<li>${alert.message} (Severity: ${alert.severity})</li>`).join('') + '</ul>';
    }

    // Function to populate recent activities
    function populateRecentActivities(activities) {
        const activitiesContainer = document.getElementById('recent-activities');
        activitiesContainer.innerHTML = '<h3>Recent Activities</h3><ul>' + activities.map(activity => `<li>${activity.description} - ${activity.timestamp}</li>`).join('') + '</ul>';
    }

    // Function to view incident details
    window.viewIncidentDetails = function(incidentId) {
        fetch(`/incident/${incidentId}`)
            .then(response => response.json())
            .then(details => {
                if (details) {
                    displayIncidentDetails(details);
                } else {
                    console.warn(`No details available for incident ${incidentId}`);
                }
            })
            .catch(error => console.error('Error fetching incident details:', error));
    };

    // Function to display incident details
    function displayIncidentDetails(details) {
        const detailContent = document.querySelector('#incident-detail-content');
        detailContent.innerHTML = `
            <h3>${details.name}</h3>
            <p><strong>ID:</strong> ${details.id}</p>
            <p><strong>Status:</strong> ${details.status}</p>
            <p><strong>Priority:</strong> ${details.priority}</p>
            <p><strong>Timestamp:</strong> ${details.timestamp}</p>
            <p><strong>Source:</strong> ${details.source}</p>
            <p><strong>Message:</strong> ${details.message}</p>
        `;
    }
});
