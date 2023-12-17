class Api::Exposed::V1::StudentsController < Api::Exposed::V1::BaseController
  def index
    respond_with course.students, each_serializer: Api::Exposed::V1::StudentSerializer
  end

  def show
    respond_with student || raise(ActiveRecord::RecordNotFound)
  end

  def create
    respond_with course.students.create!(student_params)
  end

  def batch_create
    respond_with params[:students].map do |student|
      course.students.create!(student.permit(:display_name, attendance_codes: []))
    end
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
    @student ||= course.students.by_attendance_code(params[:id]).first
  end

  def student_params
    params.require(:student).permit(
      :display_name,
      attendance_codes: []
    )
  end
end
