CREATE TABLE IF NOT EXISTS det_filetransfer
(
fileID INT AUTO_INCREMENT,
transfer_time DATETIME,
last_operation_date DATETIME,
status VARCHAR(100),
PRIMARY KEY (fileID)
);
CREATE TABLE IF NOT EXISTS det_runfiles(
    FileID INT,
    Identifier INT AUTO_INCREMENT,
    split_index VARCHAR(100),
    filename VARCHAR(255),
    Md5sum VARCHAR(255),
    filesize FLOAT,
    filesID INT,
    PRIMARY KEY (Identifier),
    FOREIGN KEY (fileID) REFERENCES det_filetransfer(fileID)
);
CREATE TABLE IF NOT EXISTS det_shifter
(
ShifterID INT AUTO_INCREMENT,
Name VARCHAR(255),
Surname VARCHAR(255),
institute VARCHAR(255),
mail VARCHAR(100),
PRIMARY KEY(ShifterID)
);

CREATE TABLE IF NOT EXISTS det_detdata
(
    Run_date DATETIME,
	ID INT AUTO_INCREMENT,
    run_number INT,
    run_file_ID INT,
    type_Profile VARCHAR(255),
    Run_Start DATETIME,
    Run_End DATETIME,
    ShifterID INT,
    Detector_configuration INT,
    comment VARCHAR(255),
    PRIMARY KEY (ID),
    FOREIGN KEY (run_file_ID) REFERENCES det_runfiles(Identifier),
    FOREIGN KEY (ShifterID) REFERENCES det_shifter(ShifterID)
);

CREATE TABLE IF NOT EXISTS det_ccfile
(
c_fileID INT AUTO_INCREMENT,
run_number INT,
det_detdataID INT,
split_index VARCHAR(100),
Filepath VARCHAR (255), 
Filename VARCHAR (100),
Filesize FLOAT,
Md5sum VARCHAR(255),
reco_level VARCHAR(255),
Status VARCHAR(100),
creation_date DATETIME,
PRIMARY KEY (c_fileID),
FOREIGN KEY (det_detdataID) REFERENCES det_detdata(ID)
);



#MySQL Workbench 
