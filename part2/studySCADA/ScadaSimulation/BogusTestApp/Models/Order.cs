using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace BogusTestApp.Models
{
    internal class Order        // 주문 테이블
    {
        public Guid Id { get; set; }
        public DateTime Date { get; set; }
        public decimal OrderValue { get; set; }
        public bool Shipped { get; set; }   // 주문 선적여부
    }
}
