
function gradingStudents(grades) {
    // Write your code here
    const roundedGrades= [];
    for(let i=0;i<grades.length;i++){
        const grade = grades[i];
        
        if(grade >  38){
            const mod = grade % 5;
            if( mod < 3){
                const newGrade = ((grade - mod)/5 + 1) * 5
                roundedGrades.push(newGrade)
            }
            else{
                roundedGrades.push(grade);
            }
        }
        else{
            roundedGrades.push(grade);
        }
        
    }
    return roundedGrades;
}
