
CREATE TABLE DEPT(DEPTNO INT NOT NULL, DNAME CHAR(14),LOC CHAR(13),CONSTRAINT DEPT_PRIMARY_KEY PRIMARY KEY (DEPTNO));

INSERT INTO DEPT VALUES (10,'ACCOUNTING','NEW YORK');

INSERT INTO DEPT VALUES (20,'RESEARCH','DALLAS');

INSERT INTO DEPT VALUES (30,'SALES','CHICAGO');

INSERT INTO DEPT VALUES (40,'OPERATIONS','BOSTON');




CREATE TABLE EMP(EMPNO INT NOT NULL,ENAME CHAR(10),JOB CHAR(9),MGR INT CONSTRAINT EMP_SELF_KEY REFERENCES EMP (EMPNO),HIREDATE DATE,SAL INT,COMM INT,DEPTNO INT NOT NULL,CONSTRAINT EMP_FOREIGN_KEY FOREIGN KEY (DEPTNO) REFERENCES DEPT (DEPTNO),CONSTRAINT EMP_PRIMARY_KEY PRIMARY KEY (EMPNO));



INSERT INTO EMP VALUES (7839,'KING','PRESIDENT',NULL,'17-NOV-1981',5000,NULL,10);

INSERT INTO EMP VALUES (7698,'BLAKE','MANAGER',7839,'1-MAY-1981',2850,NULL,30);

INSERT INTO EMP VALUES (7782,'CLARK','MANAGER',7839,'9-JUN-1981',2450,NULL,10);

INSERT INTO EMP VALUES (7566,'JONES','MANAGER',7839,'2-APR-1981',2975,NULL,20);

INSERT INTO EMP VALUES (7654,'MARTIN','SALESMAN',7698,'28-SEP-1981',1250,1400,30);

INSERT INTO EMP VALUES (7499,'ALLEN','SALESMAN',7698,'20-FEB-1981',1600,300,30);

INSERT INTO EMP VALUES (7844,'TURNER','SALESMAN',7698,'8-SEP-1981',1500,0,30);

INSERT INTO EMP VALUES (7900,'JAMES','CLERK',7698,'3-DEC-1981',950,NULL,30);

INSERT INTO EMP VALUES (7521,'WARD','SALESMAN',7698,'22-FEB-1981',1250,500,30);

INSERT INTO EMP VALUES (7902,'FORD','ANALYST',7566,'3-DEC-1981',3000,NULL,20);

INSERT INTO EMP VALUES (7369,'SMITH','CLERK',7902,'17-DEC-1980',800,NULL,20);

INSERT INTO EMP VALUES (7788,'SCOTT','ANALYST',7566,'09-DEC-1982',3000,NULL,20);

INSERT INTO EMP VALUES (7876,'ADAMS','CLERK',7788,'12-JAN-1983',1100,NULL,20);

INSERT INTO EMP VALUES (7934,'MILLER','CLERK',7782,'23-JAN-1982',1300,NULL,10);


SELECT E2.ENAME AS "MANAGER NAME",COUNT(E1.EMPNO) AS "NO_OF_EMP"
FROM EMP AS E1, EMP AS E2
WHERE E1.MGR = E2.EMPNO
GROUP BY E2.ENAME,E2.EMPNOX
