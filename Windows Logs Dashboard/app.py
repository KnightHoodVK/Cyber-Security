from flask import Flask, jsonify, render_template
import win32evtlog
from datetime import datetime

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
        
        for event in events[:5]:  # Adjust the number of events as needed
            # Format the timestamp
            timestamp_str = event.TimeGenerated.Format()
            
            # Convert the timestamp to a more readable format
            try:
                # Use the correct format string for parsing
                timestamp = datetime.strptime(timestamp_str, "%a %b %d %H:%M:%S %Y")
                formatted_timestamp = timestamp.strftime("%a %b %d %H:%M:%S %Y")
            except ValueError as e:
                formatted_timestamp = f"Error parsing date: {e}"

            # Use event.StringInserts if available
            description = " ".join(event.StringInserts) if event.StringInserts else "No description available"

            logs.append({
                'timestamp': formatted_timestamp,
                'event_id': event.EventID,
                'source': event.SourceName,
                'category': event.EventCategory,
                'description': description
            })
        
        # Close the event log handle
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

@app.route('/severities')
def severities():
    # Example implementation for severities (update as needed)
    pass

if __name__ == '__main__':
    app.run(debug=True)
