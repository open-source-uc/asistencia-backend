class Api::Internal::StudentsController < Api::Internal::BaseController
  def index
    respond_with course.students
  end

  def show
    respond_with student
  end

  def create
    respond_with course.students.create!(student_params)
  end

  def update
    student.update!(student_params)
    respond_with student
  end

  def destroy
    respond_with student.destroy!
  end

  private

  def course
    @course ||= current_user.courses.friendly.find(params[:course_id])
  end

  def student
    @student ||= course.students.find(params[:id])
  end

  def student_params
    params.require(:student).permit(
      :attendance_codes
    )
  end
end
