class SortingArray
  # assuming values is a sorted array of numbers
  # could also just use values.bsearch, but that's no fun
  def binary_search(values, target)
    middle = values.length/2

    if values[middle] == target
      middle
    elsif values.length > 1
      if values[middle] > target
        binary_search(values[0..(middle-1)], target)
      else
        index = binary_search(values[(middle+1)..-1], target)

        if index
          index + middle + 1 # when searching right side of array, returned index will not be correct index in original array
        end
      end
    end
  end

  def merge_sort(values)
    middle = values.length/2

    if values.length == 2 # if length == 1, array is implicitly sorted
      first_value = values[0]
      second_value = values[1]
      if first_value > second_value
        values[0] = second_value
        values[1] = first_value
      end

    elsif values.length > 2
      left_side = merge_sort(values[0..(middle-1)])
      right_side = merge_sort(values[middle..-1])

      values = merge_sorted_arrays(values, left_side, right_side)
    end

    values
  end

  # this would be better if swaps were done in place (and if divided into reasonably sized methods)
  def quick_sort(values, pivot_type: :random) # accepts pivot types :last, :median, and :random
    if values.length < 2 # array doesn't need sorting
      values
    else
      pivot_index = choose_pivot(values, pivot_type)
      pivot_value = values[pivot_index]
      left_pointer = 0
      right_pointer = values.length - 1


      while left_pointer < right_pointer
        left_value = values[left_pointer]
        right_value = values[right_pointer]

        if (left_value > pivot_value) && (right_value < pivot_value)
          values[left_pointer] = right_value
          values[right_pointer] = left_value
        end

        # increment pointers if values are correctly positioned
        if values[left_pointer] <= pivot_value
          left_pointer += 1
        end
        if values[right_pointer] >= pivot_value
          right_pointer -= 1
        end
      end

      # pointers have crossed, so:
      # right_pointer is now the last value of lesser side of array
      # left_pointer is now the first value of greater side of array
      # OR pointers are equal; then move one pointer so the above assumptions are true
      if (pivot_index != left_pointer) && (pivot_index != right_pointer) # pivot value is not correctly positioned between both sides of the array
        if right_pointer == left_pointer # if pointers are equal, move one so array is correctly partitioned
          if values[right_pointer] > pivot_value
            right_pointer -= 1
          elsif values[left_pointer] < pivot_value
            left_pointer += 1
          end
        end

        if right_pointer < pivot_index # pivot_index is on greater side of array
          values[pivot_index] = values[left_pointer] # swap pivot value with first greater value
          values[left_pointer] = pivot_value
          pivot_index = left_pointer
        elsif left_pointer > pivot_index
          values[pivot_index] = values[right_pointer]
          values[right_pointer] = pivot_value
          pivot_index = right_pointer
        end
      end

      # recursively sort both sides of array (taking into account that pivot could be at beginning or end)
      if pivot_index == 0
        sorted_left_side = []
      else
        sorted_left_side = quick_sort(values[0..(pivot_index-1)], pivot_type: pivot_type)
      end

      if pivot_index == (values.length - 1)
        sorted_right_side = []
      else
        sorted_right_side = quick_sort(values[(pivot_index+1)..-1], pivot_type: pivot_type)
      end

      sorted_left_side + [pivot_value] + sorted_right_side
    end
  end

  private

  # merge sort helper method
  def merge_sorted_arrays(original, left, right)
    left_pointer = 0
    right_pointer = 0

    # merge sorted arrays
    for index in (0..(original.length-1))
      if left_pointer >= left.length # pointer has passed the end of the array
        original[index] = right[right_pointer]
        right_pointer +=1

      elsif right_pointer >= right.length
        original[index] = left[left_pointer]
        left_pointer += 1

      elsif left[left_pointer] < right[right_pointer]
        original[index] = left[left_pointer]
        left_pointer += 1

      else
        original[index] = right[right_pointer]
        right_pointer += 1
      end
    end

    original
  end

  # quick sort helper method
  def choose_pivot(values, pivot_type)
    if pivot_type == :last
      values.length - 1

    elsif pivot_type == :median # pivot is median of first, middle, and last elements
      choices = [values[0], values[values.length/2], values[-1]]
      median = choices.sort[1] # using Ruby's #sort feels a bit like cheating...

      case median
      when values[0]
        0
      when values[values.length/2]
        values.length/2
      when values[-1]
        values.length - 1
      end

    else # defaults to random
      rand(values.length)
    end
  end
end
