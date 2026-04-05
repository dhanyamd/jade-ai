/**
 * Calculator function supporting basic arithmetic operations.
 *
 * @param {number} a - First operand
 * @param {string} operation - Operation: '+', '-', '*', '/'
 * @param {number} b - Second operand
 * @returns {number} Result of the operation
 * @throws {Error} If the operation is unsupported or division by zero occurs
 */
function calculator(a, operation, b) {
  switch (operation) {
    case "+":
      return a + b;
    case "-":
      return a - b;
    case "*":
      return a * b;
    case "/":
      if (b === 0) {
        throw new Error("Division by zero is not allowed");
      }
      return a / b;
    default:
      throw new Error(`Unsupported operation: ${operation}`);
  }
}

module.exports = calculator;
