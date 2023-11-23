class Course < ApplicationRecord
  resourcify

  has_many :students, dependent: :destroy
  has_many :activities, dependent: :destroy

  validates :name,
            presence: true
end

# == Schema Information
#
# Table name: courses
#
#  id         :bigint(8)        not null, primary key
#  name       :string           not null
#  enabled    :string           default("t"), not null
#  created_at :datetime         not null
#  updated_at :datetime         not null
#
