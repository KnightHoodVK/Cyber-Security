from flask import Flask, jsonify, render_template
import win32evtlog
from datetime import datetime
import psutil  # Ensure psutil is installed (`pip install psutil`)

app = Flask(__name__)

def get_logs(log_type):
    logs = []
    server = 'localhost'
    log_types = {
        'application': 'Application',
        'system': 'System',
        'security': 'Security'
    }
    log_type = log_types.get(log_type.lower(), 'Application')
    
    try:
        handle = win32evtlog.OpenEventLog(server, log_type)
        events = win32evtlog.ReadEventLog(handle, win32evtlog.EVENTLOG_FORWARDS_READ | win32evtlog.EVENTLOG_SEQUENTIAL_READ, 0)
        
        for event in events[0:]:  # Adjust the number of events as needed
            timestamp_str = event.TimeGenerated.Format()
            try:
                timestamp = datetime.strptime(timestamp_str, "%a %b %d %H:%M:%S %Y")
                formatted_timestamp = timestamp.strftime("%a %b %d %H:%M:%S %Y")
            except ValueError as e:
                formatted_timestamp = f"Error parsing date: {e}"

            description = " ".join(event.StringInserts) if event.StringInserts else "No description available"

            logs.append({
                'timestamp': formatted_timestamp,
                'event_id': event.EventID,
                'source': event.SourceName,
                'category': event.EventCategory,
                'message': description
            })
        
        win32evtlog.CloseEventLog(handle)
        
    except Exception as e:
        print(f"Error reading logs: {e}")
    
    return logs

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logs/<log_type>')
def logs(log_type):
    return jsonify(get_logs(log_type))

@app.route('/incidents')
def incidents():
    application_logs = get_logs('application')
    incidents = [
        {
            'id': index + 1,
            'name': f"Log {index + 1}",
            'status': 'Open',
            'priority': 'High',
            'timestamp': log['timestamp'],
            'source': log['source'],
            'message': log['message']
        }
        for index, log in enumerate(application_logs)
    ]
    return jsonify(incidents)

@app.route('/playbook-steps')
def playbook_steps():
    playbook_steps = [
        {'description': 'Preparation: Establish and maintain an incident response capability'},
        {'description': 'Detection and Analysis: Detect and analyze incidents'},
        {'description': 'Containment, Eradication, and Recovery: Contain, eradicate, and recover from incidents'},
        {'description': 'Post-Incident Activity: Conduct post-incident activities, including lessons learned'}
    ]
    return jsonify(playbook_steps)

@app.route('/incident/<int:incident_id>')
def incident_detail(incident_id):
    application_logs = get_logs('application')
    incident_details = next(({
        'id': index + 1,
        'name': f"Log {index + 1}",
        'status': 'Open',
        'priority': 'High',
        'timestamp': log['timestamp'],
        'source': log['source'],
        'message': log['message']
        } for index, log in enumerate(application_logs) if index + 1 == incident_id), {})
    return jsonify(incident_details)

@app.route('/system-health')
def system_health():
    try:
        cpu_usage = psutil.cpu_percent(interval=1)
        memory_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent
        
        return jsonify({
            'cpuUsage': cpu_usage,
            'memoryUsage': memory_usage,
            'diskSpace': disk_usage
        })
    except Exception as e:
        print(f"Error fetching system health: {e}")
        return jsonify({'error': 'Unable to fetch system health data'}), 500

@app.route('/active-alerts')
def active_alerts():
    # Sample data for active alerts
    alerts = [
        {'message': 'CPU usage is high', 'severity': 'Critical'},
        {'message': 'Disk space running low', 'severity': 'Warning'}
    ]
    return jsonify(alerts)

@app.route('/incident-summary')
def incident_summary():
    try:
        application_logs = get_logs('application')
        total_incidents = len(application_logs)
        open_incidents = total_incidents  # For simplicity, assuming all are open
        closed_incidents = 0  # Assuming no closed incidents for now
        
        return jsonify({
            'totalIncidents': total_incidents,
            'openIncidents': open_incidents,
            'closedIncidents': closed_incidents
        })
    except Exception as e:
        print(f"Error fetching incident summary: {e}")
        return jsonify({'error': 'Unable to fetch incident summary'}), 500

@app.route('/recent-activities')
def recent_activities():
    # Sample data for recent activities
    activities = [
        {'description': 'Reviewed security logs', 'timestamp': '2024-08-26 14:32:00'},
        {'description': 'Updated firewall rules', 'timestamp': '2024-08-26 13:15:00'}
    ]
    return jsonify(activities)

if __name__ == '__main__':
    app.run(debug=True)
