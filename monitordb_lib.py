from sqlalchemy import create_engine, MetaData, Table, String, Float, Column

def luigiDBInit():
	# Initializes luigi database with the appropriate env variables
	#
	# Returns the connection and luigi table for SQL operations,
	# but abstracts the table's columns, db engine, and metadata.
	db = create_engine('postgresql://{}:{}@db/{}'.format(os.getenv("POSTGRES_USER"), os.getenv("POSTGRES_PASSWORD"), os.getenv("POSTGRES_DB")), echo=False)
	conn = db.connect()
	luigi = Table('luigi', MetaData(db),
    	          Column("luigi_job", String(100)),
    	          Column("status", String(20)),
    	          Column("submitter_specimen_id", String(100)),
	              Column("specimen_uuid", String(100)),
	              Column("workflow_name", String(100)),
	              Column("center_name", String(100)),
	              Column("submitter_donor_id", String(100)),
	              Column("consonance_job_uuid", String(100), primary_key=True),
	              Column("submitter_donor_primary_site", String(100)),
	              Column("project", String(100)),
	              Column("analysis_type", String(100)),
	              Column("program", String(100)),
	              Column("donor_uuid", String(100)),
	              Column("submitter_sample_id", String(100)),
	              Column("submitter_experimental_design", String(100)),
	              Column("submitter_specimen_type", String(100)),
	              Column("workflow_version", String(100)),
	              Column("sample_uuid", String(100)),
	              Column("start_time", String(100)),
	              Column("last_updated", String(100)))

	if not db.dialect.has_table(db, luigi):
	    luigi.create()

	return conn, luigi